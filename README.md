# WeRe


## Contents
  - [Contents](#contents)
  - [Long description](#long-description)
    - [What's the problem?](#whats-are-we-building)
    - [The idea](#the-key-idea-and-its-advantages)
    - [How can technology help?](#what-problems-are-being-solved)
  - [The architecture](#the-architecture)
  - [Project roadmap](#project-roadmap)
  - [Demo video](#demo-video)
  - [Built with](#built-with)



## Long description

### What's the problem?
  In India, 77% of waste is disposed of in open dumps, 18% is composted and just 5% is recycled. Among the 77%, a certain percentage of the waste is recyclable but is mixed with common trash. We are currently facing the crisis of landfill overflow and increasing waste production. 
But a change in this appraisal can be made if we practice segregating waste instead of discharging mixed waste.
Especially in villages, there is no mechanism or service by the administration to recycle or collect trash. 
As a result, many villages just innocently burn it or dump it in the open, despite numerous establishments and industries that take in and create recycled products. 

### What we are building: 

Our goal is to reach every household, providing them with the service of making use of their recyclable waste. We are building a network that connects ordinary citizens to industries, by collecting and transporting recyclable waste to the establishments that require them.
Users of our system include      the residents in the local region, the volunteers for the job and buyers/industries


#### Role of residential users -
  The residents of the locality must register themselves through the website. They are obliged to separate recyclable wastes such as paper, plastic, and textiles. Volunteers/collectors shall set a limit on the amount of waste they can handle. Once that limit is reached in a household, the user can send an alert message to the collector.


#### Role of Collectors/Volunteers/Drivers -
  Collectors/volunteers of a particular region are informed about the status of each household. Our main intention is to offer these duties to the local women organizations (such as ‘Kudumbashree’ in Kerala) to collaborate with women to take a stand in saving our environment.
Also since India is behind on part-time job culture, students of age 16 and above can volunteer in the collection process. 
Women are also encouraged to take on transportation duties from the assigned locality to the industries.
Working hours and regions of action shall be flexible and friendly to the volunteers. 

#### Role of Buyers/Industries -
  These involve the establishments that work on creating recycled products. Heaps of segregated waste are transported from localities to these industries. 

## The key idea and its advantages
  We have come up with a platform where people can get rid of the recyclable waste in their house with ease.What we would like to acheive through this is to create a self-sustaining platform that would be benificial to the users directly as well as take a step towards saving the enviornment also. A model like the one we propose has many advantages like reducing the need to set up infrastructure and handle logistics .This in turn gives us the power to expand freely and efficeintly in a manner which is not possible for any other organization.It also offers the customer a great degree of felxibilty in almost every aspect they can think of, be it collection or delivery.We want these processes to be carried out as a part of their normal ddaily routine without consuming any additional time or resources. That is where the real strength of our approach lies.
  
### What problems are being solved:

People now have a medium to reduce the amount of wastage they produce and burn on a daily basis. Recyclable wastes are put to use. Overflowing landfills are avoided.
Women are given job opportunities and they help in sustaining the environment. Young adults can take action on recycling and have an opportunity to earn via part-time jobs.
Once every household builds up the habit of recycling, we are one step towards waste-reduction and tackling climate change.

## The architecture

![Alt text](https://i1.wp.com/blog.mi.hdm-stuttgart.de/wp-content/uploads/2019/08/architecture.jpeg?w=802&ssl=1)

1. The user navigates to the site and logs in.
2. They can creates an account with us if they havent done so already.
3. The user selects the type of material and clicks on raise pickup.
4. This information is given provided to volunteers nearby, who then collects it.
5. The local voluteers can then raise pickup when they have sufficient items.
6. Volunteers registered as driver to haul shipments would then come collect this and take it to recycling centers directly.

*All users would be able to earn a small amount for thier efforts to save earth
*We wish to offer maximum flexibily in all the steps mentioned above to make is as convenient as possible

## Project roadmap

The project currently does the following things.

- A user(residents) could sell the recyclable waste they have hassle free with no work whatsoever
- A user(mainly college students and local women organization) could volunteer to help in 
  getting the items from house to plants and earn an income in doing so
- A user(Recycling companies) could also buy these 

*We currently take plastics and old garments

- We identified the needs of the primary target group for our projet and also the problems they face 
- We decided to create the product as a web app with flask to handle the backend
- We designed an interactive easy to use User Interface keeping in mind accessibilty
- Developed the basic backend structure
- Set up a mysql database
- Added the user login mechanism
- Repackaged the entire application
- Prepare to deploy to cloud (configured the app)
- Create the needed resources on ibm cloud
- Deployed the application
- Fixed all bugs 
- Completed basic testing
- Supplied to project to a few friends and made a few changes based on their feedback
- Deployed the final iteration application
 
 We intend to expand in terms of both availability as well as items that we collect. As mentioned this is one of the string suits of our idea. 
 We would also like to add android and ios support in the near future.Another area we like to concentrate is introducing customized support system for each collector
 based on his daily routes as well as real time tracking of shipments.

## Demo video

You can watch the demo video here - https://youtu.be/adCAYVdu4ZQ

UI Design link - https://www.figma.com/file/loEGZMKISFUN1mdPfdWcq0/Ksum-Hackathon?node-id=0%3A1
## Built with

- [IBM Cloud Foundry](https://cloud.ibm.com/catalog?search=cloud%20functions#search_results) - The multi-cloud platform used to support the development, management and continuous delivery of web applications.
- [MySQL Database](https://www.mysql.com/) - The database used
- [Flask(https://flask.palletsprojects.com/en/2.0.x/) - The python based web framework that we used
- [Bootstrap](https://getbootstrap.com/) - The open source front end framework used

