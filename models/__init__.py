from .armhubert import model as armhubert
from .maskhubert import model as maskhubert
from .starhubert import model as starhubert


def init_model(model_name):
    model_config_dict = {
                        'armhubert': armhubert.CustomStudentModelConfig,
                        'maskhubert': maskhubert.CustomStudentModelConfig,
                        'armwavlm': armhubert.CustomStudentModelConfig,  # ARMwavLM shares the same student model with ARMHuBERT
                        'starhubert': starhubert.CustomStudentModelConfig
    }

    model_dict = {
                'armhubert': armhubert.CustomStudentModel,
                'maskhubert': maskhubert.CustomStudentModel,
                'armwavlm': armhubert.CustomStudentModel,  # ARMwavLM shares the same student model with ARMHuBERT
                'starhubert': starhubert.CustomStudentModel
    }
    
    if model_name in model_config_dict:
        return model_config_dict[model_name], model_dict[model_name]
    else:
        raise NotImplementedError
