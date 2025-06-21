# Portfolio Site

This portfolio site serves as an update built on the back of the [MLH Fellowship PE Portfolio Template](https://github.com/MLH-Fellowship/pe-portfolio-site).
It aims to prioritize adaptability through the use of json and jinja.

## Getting Started
### Altering content
All adaptable content for the website is stored in the "content.json" file. For content that is singleton like e.g the about me section it can be altered using its corresponding json entry. e.g content.json["about"] where relevant subgields of the piece of content for example the "title" can also be changed which will reflect on the website.

Content which can have multiple entries for example, hobbies, education, jobs are lists within the content.json which can be added to or subtracted from freely. The use of jinja allows the display of any number of these items without compromising the structural integrity of the site.

## Features 
### Photo of yourself.

The placeholder photo and location which it is to be specified in have been changed for easier access. It has been moved to the content.json along with the rest of the program's input in an effort to make updating the website more painless.

### About yourself.
The user is able to specify the title and content of the "About Yourself" section in the content.json file.

### Work Experience.
The ability to seamlessly add work experience has been accomplished by using html and jinja and the content.json allowing those sections the user to painlessly add as any jobs as they like, there is a default value for the job's end date, setting it to "present".

### Hobbies.
A seperate page listing the hobbies featuring images and descriptions has been added, the description has an empty string as a default value in case the user does not want to describe a given hobby. Like work experience, any amount of hobbies can be added to the site seamlessly without compromising its functionality. 

### Education.
The education section allows users to specify their previous education in varying levels of detail. The end date variable has a default value of present for those still in education. In addition, the grade and skills sections are also optional.

### Travel Map.
The travel map has been added to the home page, allowing the site owner to specify any number of visited countries using the content.json to specify the country name and location on the map.


## Installation

Make sure you have python3 and pip installed

Create and activate virtual environment using virtualenv
```bash
$ python -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies!

```bash
pip install -r requirements.txt
```

## Usage

Create a .env file using the example.env template (make a copy using the variables inside of the template)

Start flask development server
```bash
$ export FLASK_ENV=development
$ flask run
```

You should get a response like this in the terminal:
```
❯ flask run
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

You'll now be able to access the website at `localhost:5000` or `127.0.0.1:5000` in the browser! 

*Note: The portfolio site will only work on your local machine while you have it running inside of your terminal. We'll go through how to host it in the cloud in the next few weeks!* 

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
