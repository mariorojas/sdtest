# Test script for Stable Diffusion

## Installation commands

```
git clone https://github.com/mariorojas/sdtest.git
cd sdtest/
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

Make sure to get your [Stable Diffusion API key](https://platform.stability.ai/docs/getting-started/authentication) and set it in **main.py**

```
os.environ['STABILITY_KEY'] = 'your-stable-diffusion-key'
```

To create an image, run the following:

```
python main.py
# output: 2054418320.png
```

To create more than 1 image, increase `sample` value in **main.py**.

Please consider this value can increase credit cost.

```
answers = stability_api.generate(
    ...
    samples=1
)
```
