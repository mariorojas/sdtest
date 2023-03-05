import io
import os
import warnings

import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
from PIL import Image
from stability_sdk import client

os.environ['STABILITY_HOST'] = 'grpc.stability.ai:443'
os.environ['STABILITY_KEY'] = 'your-stable-difussion-key'

stability_api = client.StabilityInference(
    key=os.environ['STABILITY_KEY'],
    verbose=True,
    engine="stable-diffusion-v1-5",
)

answers = stability_api.generate(
    prompt="a teenager hacker student in his mid 20s using a hoodie, clean cel shaded vector art, shutterstock, behance hd by lois van baarle, artgerm, helen huang, by makoto shinkai and ilya kuvshinov, rossdraws, illustration",
    steps=15,
    cfg_scale=8.0,
    width=512,
    height=512,
    guidance_preset=generation.GUIDANCE_PRESET_FAST_GREEN,
    samples=1
)

for resp in answers:
    for artifact in resp.artifacts:
        if artifact.finish_reason == generation.FILTER:
            # blurry images cost no credits
            warnings.warn(
                "Your request activated the API's safety filters and could not be processed."
                "Please modify the prompt and try again."
            )
        if artifact.type == generation.ARTIFACT_IMAGE:
            img = Image.open(io.BytesIO(artifact.binary))
            img_name = str(artifact.seed) + ".png"
            img.save(img_name)
            print(img_name)
