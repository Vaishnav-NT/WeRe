# WeRe


## Contents
  - [Contents](#contents)
  - [Short description](#short-description)
    - [What's the problem?](#whats-the-problem)
    - [How can technology help?](#how-can-technology-help)
    - [The idea](#the-idea)
  - [Demo video](#demo-video)
  - [The architecture](#the-architecture)
  - [Long description](#long-description)
  - [Project roadmap](#project-roadmap)
  - [Getting started](#getting-started)
  - [Live demo](#live-demo)
  - [Built with](#built-with)
  - [Contributing](#contributing)
  - [Authors](#authors)

## Short description

### What's the problem?
  In India, 77% of waste is disposed of in open dumps, 18% is composted and just 5% is recycled. Among the 77%, a certain percentage of the waste is recyclable but is mixed with common trash. We are currently facing the crisis of landfill overflow and increasing waste production. 
But a change in this appraisal can be made if we practice segregating waste instead of discharging mixed waste.
Especially in villages, there is no mechanism or service by the administration to recycle or collect trash. 
As a result, many villages just innocently burn it or dump it in the open, despite numerous establishments and industries that take in and create recycled products. 


### The key idea


## The architecture


1. The user navigates to the site and uploads a video file.
2. Watson Speech to Text processes the audio and extracts the text.
3. Watson Translation (optionally) can translate the text to the desired language.
4. The app stores the translated text as a document within Object Storage.

## Long description

### What we are building: 

Our goal is to reach every household, providing them with the service of making use of their recyclable waste. We are building a network that connects ordinary citizens to industries, by collecting and transporting recyclable waste to the establishments that require them.
Users of our system include      the residents in the local region, the volunteers for the job and buyers/industries.

#### Role of residential users -
  The residents of the locality must register themselves through the website. They are obliged to separate recyclable wastes such as paper, plastic, and textiles. Volunteers/collectors shall set a limit on the amount of waste they can handle. Once that limit is reached in a household, the user can send an alert message to the collector.


#### Role of Collectors/Volunteers/Drivers -
  Collectors/volunteers of a particular region are informed about the status of each household. Our main intention is to offer these duties to the local women organizations (such as ‘Kudumbashree’ in Kerala) to collaborate with women to take a stand in saving our environment.
Also since India is behind on part-time job culture, students of age 16 and above can volunteer in the collection process. 
Women are also encouraged to take on transportation duties from the assigned locality to the industries.
Working hours and regions of action shall be flexible and friendly to the volunteers. 

#### Buyers -
  These involve the establishments that work on creating recycled products. Heaps of segregated waste are transported from localities to these industries. 


### What problems are being solved:

People now have a medium to reduce the amount of wastage they produce and burn on a daily basis. Recyclable wastes are put to use. Overflowing landfills are avoided.
Women are given job opportunities and they help in sustaining the environment. Young adults can take action on recycling and have an opportunity to earn via part-time jobs.
Once every household builds up the habit of recycling, we are one step towards waste-reduction and tackling climate change.

## Project roadmap

The project currently does the following things.

- Feature 1
- Feature 2
- Feature 3

It's in a free tier IBM Cloud Kubernetes cluster. In the future we plan to run on Red Hat OpenShift, for example.

See below for our proposed schedule on next steps after Call for Code 2021 submission.

## Demo video

## Live demo

You can find a running system to test at [callforcode.mybluemix.net](https://were.eu-gb.cf.appdomain.cloud/).

## Built with

- [IBM Cloudant](https://cloud.ibm.com/catalog?search=cloudant#search_results) - The NoSQL database used
- [IBM Cloud Foundry](https://cloud.ibm.com/catalog?search=cloud%20functions#search_results) - The multi-cloud platform used to support the development, management and continuous delivery of web applications.
- [Flask(https://flask.palletsprojects.com/en/2.0.x/) - The python based web framework that we used
- [Bootstrap](https://getbootstrap.com/) - The open source front end framework used


## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

<a href="https://github.com/Call-for-Code/Project-Sample/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=Call-for-Code/Project-Sample" />
</a>
