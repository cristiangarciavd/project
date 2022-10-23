var reporter = require("cucumber-html-reporter");

var options = {
  theme: "bootstrap",
  jsonFile: "./reports/cucumber_report.json",
  output: "./reports/cucumber_report.html",
  reportSuiteAsScenarios: true,
  scenarioTimestamp: true,
  launchReport: true,
  metadata: {
    "Testing Framework": "Trello API & UI",
    "Test Environment": "STAGING",
  },
};

reporter.generate(options);
