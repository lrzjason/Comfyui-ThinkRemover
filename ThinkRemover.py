
import torch
import numpy as np
import cv2

    
# make the perfect mask for in context lora
# scale the mask to maximum 4x and minium 0.25x
# full pixel usage with 768x1024 context window
class ThinkRemover:
    @classmethod
    def INPUT_TYPES(s):
        return {
                "required": { 
                    "text": ("STRING",),
                    
                },
                "optional":{
                }
            }
    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("cleared_content", "think_content")
    FUNCTION = "think_remover"
    CATEGORY = "ThinkRemover/ThinkRemover"
    
    
    def think_remover(self, text):
        cleared_content = text
        think_content = text
        think_tag = '</think>'
        # check text contains '</think>'
        if think_tag in text:
            # get index of '</think>'
            end_index = text.index(think_tag)+len(think_tag)
            think_content = text[:end_index].strip()
            cleared_content = text[end_index+1:].strip()
        
        return (cleared_content, think_content)

if __name__ == "__main__":
    # test the module
    think_remover = ThinkRemover()
    cleared_content, think_content = think_remover.think_remover("<think>I am thinking about this.</think> I am doing something else.")
    print(cleared_content)
    print(think_content)