# talk-preview-img-builder

A tool helps build a talk preview image by combining the given background image and talk event description

## Installation and Usage

### Install Dependencies

For running the app, you need to install the following dependencies by following command:

```bash
pipenv install -d
```

### Run the Application

Before running the application, you need to prepare the material for building the talk preview images/slides.
There are two materials that are required:

- A background image named `background.png`  which is located in the `materials/img` folder.

- A talk event description named `speeches.json` which is located in the `materials/` folder.

After preparing the material, you can run the application by following command:

```bash
pipenv run build_talk_preview_img   # build the talk preview images
```

or

```bash
pipenv run build_talk_preview_ppt  # build the talk preview slides
```

The generated talk preview images and slides are located in the `export/` folder.

### Configuring the Application

There are several options to configure the application, the default values are shown in the `config.py` file.
You can override the default values by editing the `config.py` file or adding a `.env` file that setting theses variables before running the app.

| Variable | Description | Default Value (Setting for Image/ Setting for Slides) | Type (Setting for Image/ Setting for Slides) |
| -------- | -------- | ------------- | -------- |
| BACKGROUND_IMG_PATH | The path to the background image | `materials/img/background.png` | String |
| SPEECHES_PATH  | The path to the speech description | `materials/speeches.json` | String |
| PREVIEW_IMG_WIDTH     | The width of the generated preview image  |  700px / 30cm  | Integer / Float |
| PREVIEW_IMG_HEIGHT    | The height of the generated preview image  |  700px / 30cm  | Integer / Float |
| PREVIEW_IMG_TITLE_UPPER_LEFT_X | The left position of the title in the upper left corner of the generated preview image  |  110px / 0.95cm  | Integer / Float |
| PREVIEW_IMG_TITLE_UPPER_LEFT_Y | The top position of the title in the upper left corner of the generated preview image  |  110px / 1.04cm  | Integer / Float |
| PREVIEW_IMG_CONTENT_UPPER_LEFT_X | The left position of the content in the upper left corner of the generated preview image  |  85px / 1.38cm  | Integer / Float |
| PREVIEW_IMG_CONTENT_UPPER_LEFT_Y | The top position of the content in the upper left corner of the generated preview image  |  200px / 3.8cm  | Integer / Float |
| PREVIEW_IMG_FOOTER_UPPER_LEFT_X | The left position of the footer in the upper left corner of the generated preview image  |  100px / 1.6cm  | Integer / Float |
| PREVIEW_IMG_FOOTER_UPPER_LEFT_Y | The top position of the footer in the upper left corner of the generated preview image  |  650px / 12.2cm  | Integer / Float |
| PREVIEW_IMG_SPEAKER_UPPER_RIGHT_X | The right position of the speaker name in the upper right corner of the generated preview image  |  600px / 13.5cm  | Integer / Float |
| PREVIEW_IMG_SPEAKER_UPPER_RIGHT_Y | The top position of the speaker name in the upper right corner of the generated preview image  |  570px / 10cm  | Integer / Float |
| TITLE_HEIGHT | The height of the title  |  70px / 1.84cm  | Integer / Float |
| CONTENT_HEIGHT | The height of the content | 90px / 7.5cm | Integer / Float |
| PREVIEW_TEXT_COLOR | The color of text used in the preview image | #080A42  | String |
| PREVIEW_HIGHTLIGHT_TEXT_COLOR | The highlight color of text used in the preview image | #EBCC73  | String |
| PREVIEW_TEXT_FONT | The font used in the preview image | "PingFang.ttc"/"Taipei Sans TC Beta" | String |
| PREVIEW_TEXT_BOLD_FONT | The bold font used in the preview image | "PingFang.ttc"/"Taipei Sans TC Beta" | String |

### Coding Style

The coding style of the application is PEP8. You can use the following command to check the coding style:

```bash
pipenv run lint
```

and the following command to reformat the coding style which is leveraged by `black` and `isort`:

```bash
pipenv run reformat
```

### TODO


- [ ] Automatically generate the talk preview metadata file (e.g. `speeches.json`) from the PyConTW API server.
- [ ] Implement hybrid language support text wrapping in title and content of the talk preview image.
- [ ] Implement dynamic font size adjustment in the title and content of the talk preview image depending on the length of words.
- [ ] Implement CI workflow by using GitHub Actions
