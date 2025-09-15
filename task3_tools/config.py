import json
import sys

#check
if len(sys.argv) != 2:
    sys.exit(1)

config_path = sys.argv[1]

try:
    
    with open(config_path, 'r') as file:
        config_data = json.load(file)
    #print
    print("name is：", config_data["robot_name"])
    print("health：", config_data["health"])
    print("ammo：", config_data["ammo"])
    print("enabled modules：", ", ".join(config_data["enabled_modules"]))

#the following content is from AI
except FileNotFoundError: 
    print(f"文件 {config_path} 不存在")
except json.JSONDecodeError:
    print(f"文件 {config_path} 不是有效的 JSON 格式")
except KeyError as e:
    print(f"配置文件缺少必要的键：{e}")
except Exception as e:
    print(f"发生错误：{e}")