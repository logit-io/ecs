from copy import deepcopy
from typing import (
    Dict,
)

from os.path import join

from _types import (
    Field,
    FieldNestedEntry,
)
from generators import ecs_helpers
from generators.es_template import dict_add_nested, entry_for, mapping_settings, save_json, template_settings, component_name_convention, save_component_template, save_composable_template


OPENSEARCH_REMAP = {
    'constant_keyword': 'keyword',
    'wildcard': 'keyword',
    'flattened': 'object',
    'version': 'keyword',
    'match_only_text': 'text',
}

# Composable Template


def generate(
    ecs_nested: Dict[str, FieldNestedEntry],
    ecs_version: str,
    out_dir: str,
    mapping_settings_file: str,
    template_settings_file: str
) -> None:
    """This generates all artifacts for the composable template approach"""
    all_component_templates(ecs_nested, ecs_version, out_dir)
    component_names = component_name_convention(ecs_version, ecs_nested)
    save_composable_template(ecs_version, component_names, out_dir, mapping_settings_file, template_settings_file)


def all_component_templates(
    ecs_nested: Dict[str, FieldNestedEntry],
    ecs_version: str,
    out_dir: str
) -> None:
    """Generate one component template per field set"""
    component_dir: str = join(out_dir, 'opensearch/composable/component')
    ecs_helpers.make_dirs(component_dir)

    for (fieldset_name, fieldset) in ecs_helpers.remove_top_level_reusable_false(ecs_nested).items():
        field_mappings = {}
        for (flat_name, field) in fieldset['fields'].items():
            name_parts = flat_name.split('.')
            opensearch_remap_field_type(field)  # Apply the remap function here
            dict_add_nested(field_mappings, name_parts, entry_for(field))

        save_component_template(fieldset_name, field['level'], ecs_version, component_dir, field_mappings)

# Legacy template


def generate_legacy(
    ecs_flat: Dict[str, Field],
    ecs_version: str,
    out_dir: str,
    mapping_settings_file: str,
    template_settings_file: str
) -> None:
    """Generate the opensearch index template"""
    field_mappings = {}
    for flat_name in sorted(ecs_flat):
        field = ecs_flat[flat_name]
        opensearch_remap_field_type(field)

        name_parts = flat_name.split('.')
        dict_add_nested(field_mappings, name_parts, entry_for(field))

    mappings_section: Dict = mapping_settings(mapping_settings_file)
    mappings_section['properties'] = field_mappings

    generate_legacy_template_version(ecs_version, mappings_section, out_dir, template_settings_file)


def generate_legacy_template_version(
    ecs_version: str,
    mappings_section: Dict,
    out_dir: str,
    template_settings_file: str
) -> None:
    ecs_helpers.make_dirs(join(out_dir, 'opensearch'))
    template: Dict = template_settings(ecs_version, mappings_section, template_settings_file, is_legacy=True)
    # remove order as this is not supported in opensearch
    template.pop('order')
    template.setdefault('template', {})
    copies = ['mappings', 'settings']
    for cp in copies:
        template['template'][cp] = deepcopy(template[cp])
        del template[cp]

    filename: str = join(out_dir, "opensearch/template.json")
    save_json(filename, template)


def opensearch_remap_field_type(
    field: Dict
) -> None:
    if field['type'] in OPENSEARCH_REMAP:
        typ = field['type']
        field['type'] = OPENSEARCH_REMAP[typ]

    if 'multi_fields' in field:
        for multi_field in field['multi_fields']:
            typ = multi_field['type']
            multi_field['type'] = OPENSEARCH_REMAP[typ]