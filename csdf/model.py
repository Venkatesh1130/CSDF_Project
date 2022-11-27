import hashlib
import gradio as gr



def greet(img,img1):
    
    m = hashlib.sha256()
    m1=hashlib.sha256()
    m.update(img)
    m1.update(img1)
    # print(m.hexdigest())
    # print(m1.hexdigest())
    # Image_check_hash=m.update(img1)
    
    if m.hexdigest()==m1.hexdigest():
        return "Image is not Tampered"
    else:
        return "Image is Tampered"
    # return "done"
# gr.title("Image Tampering Detection")

css_code='body{background-image:url("https://picsum.photos/seed/picsum/200/300");}'

image = gr.inputs.Image(shape = (250,250))
image1 = gr.inputs.Image(shape = (250,250))
demo = gr.Interface(fn=greet, inputs=[image,image1], outputs="text",title="Image Tampering Detection",
                    description="Image Tampering Detection using Hashing Technique",
                    css=css_code)


# demo = gr.Interface(fn=greet, inputs=image1, outputs="text")

        
    
demo.launch(auth=("venkatesh","abc123"),auth_message="Enter Username and Password to get into application")








