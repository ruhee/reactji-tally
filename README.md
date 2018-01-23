# reactji-tally

A tool that aggregates all the reactjis from a Slack channel export and puts them into a nice graph. Mostly intended for project retros and general fun.

The initial data file is not included as it is a raw history of Slack channel messages. More documentation and examples are on the way.

This project was bootstrapped with [Create React App](https://github.com/facebookincubator/create-react-app).

![graph](https://i.imgur.com/eRA4Gbh.png)

### Usage

This is a work in progress; steps to follow will be reduced eventually.

This project assumes `node 8.0.0` and `npm 5.6.0`.

* Install [slack-history-export](https://github.com/hisabimbola/slack-history-export).
* Clone this project and run `npm install` in the root directory.
* [Generate a legacy token](https://api.slack.com/custom-integrations/legacy-tokens) for the Slack instance you want to run this against.
* Follow the directions in slack-history-export for setting your token (either as an environment variable or with a flag when you invoke the script).
* Export your chosen Slack channel with slack-history-export and save it in `scripts/data.json` in this project.
* Run `npm run go` in the project. You should see a new json file appear (`src/tidied.json`) and a development server run. If it doesn't pop open a window automatically, navigate to `localhost:3000` in your browser.
