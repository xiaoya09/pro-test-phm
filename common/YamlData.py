import yaml


class Yaml_data:
    def read_yaml(self,filename):
        with open(filename, encoding="utf-8") as fs:
            data = yaml.load(stream=fs, Loader=yaml.FullLoader)
            return data


    def write_yaml(self,filePath,data):
        with open(filePath,mode="w", encoding="utf-8") as fs:
            yaml.dump(data,stream=fs,allow_unicode=True)



    def clear_yaml(self,filepath):
        with open(filepath,encoding="utf-8",mode="w") as fs:
            fs.truncate()





if __name__ == '__main__':
    import os
    from common.Path_Send import configYaml
    lll=os.path.join(configYaml,"login.yaml")
    ll=Yaml_data().read_yaml(lll)
    print(ll)



    # def write_extract_yaml(self,data):
    #     with open(configYaml("\\extracl.yaml"),mode="r", encoding="utf-8") as file:
    #         old_result = yaml.safe_load(file)
    #         if old_result is not None:
    #             for key, value in dict(data).items():
    #                 if key in old_result:
    #                     old_result[key] = value
    #                     with open(configYaml("\\extracl.yaml"), mode="w", encoding="utf-8") as replace_file:
    #                         data = yaml.dump(data=old_result, stream=replace_file, allow_unicode=True)
    #                 else:
    #                     with open(configYaml("\\extracl.yaml"), mode="a", encoding="utf-8") as add_file:
    #                         data = yaml.dump(data=data, stream=add_file, allow_unicode=True)
    #         else:
    #             with open(configYaml("\\extracl.yaml"), mode="a", encoding="utf-8") as add_file:
    #                 data = yaml.dump(data=data, stream=add_file, allow_unicode=True)
    #         return data

