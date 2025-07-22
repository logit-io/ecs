# Logit README file to avoid constant merge conflicts with main readme

To run the scripts you will need python + the dependancies installed

```
python3 -m venv venv
source venv/bin/activate
pip install -r scripts/requirements.txt
```

A current example of how to run the generator script 
```
python scripts/generator.py --ref v9.0.0 --semconv-version v1.36.0
```

The --ref refers to the ecs verions you want and may require updating this fork to get any updated tags/changes

the --semconv-version refers to the opentelemetry merging efforts, you should check https://github.com/open-telemetry/semantic-conventions for the latest/supported versions
