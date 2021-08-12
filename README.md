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

There are several options to configure the application