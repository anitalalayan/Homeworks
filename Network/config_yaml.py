with open('config.yaml', 'w') as file:
    file.write("""
server:
  host: localhost
  port: 8080
logging:
  level: INFO
  file: app.log """)

import yaml

with open('config.yaml', 'r') as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)

    print(config)

config['server']['port'] = 9090

with open('config.yaml', 'w') as file:
    fs = yaml.dump(config, file)

with open('config.yaml', 'r') as file:
    new = yaml.load(file, Loader=yaml.SafeLoader)
    print(new)

