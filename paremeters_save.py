import translation, parameters
from translation import tr_en
import json, os
import locale

lang = locale.getdefaultlocale()
if lang[0].startswith("zh"):
    default_lang = translation.language_zh
else:
    default_lang = translation.language_en

class ParametersToSave:

    def __init__(self):
        self.files = []       # kfpkg: [file path]
                        # bin files: [(path,addr,prefix,enable), ...]
        self.board    = parameters.SipeedMaixBit
        self.burnPosition = tr_en("Flash")
        self.baudRate = 2
        self.skin = 2
        self.language = default_lang
        self.slowMode = True


    def __del__(self):
        pass
    
    def save(self, path):
        data = {}
        rm = []
        for f in self.files:
            if f[0]=="" or not os.path.exists(f[0]):
               rm.append(f) 
        for f in rm:
            self.files.remove(f)
        data["files"] = self.files
        data["board"] = self.board
        data["burn_pos"] = self.burnPosition
        data["skin"] = self.skin
        data["language"] = self.language
        data["slow_mode"] = self.slowMode

        dir_path = os.path.dirname(os.path.realpath(path))
        try:
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
        except:
            pass

        try:
            with open(path, "w+") as f:
                json.dump(data, f, indent=4)
        except:
            pass
    
    def load(self, path):
        try:
            with open(path, "r") as f:
                data = json.load(f)
        except Exception as e:
            return
        try:
            self.files = data["files"]
            self.board = data["board"]
            self.burnPosition = data["burn_pos"]
            self.skin = data["skin"]
            self.language = data["language"]
            self.slowMode = data["slow_mode"]
        except Exception:
            pass

