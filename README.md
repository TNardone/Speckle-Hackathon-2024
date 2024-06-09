# Speckle-Hackathon-2024
## Inspiration
We got our inspiration from experimenting with Speckle objects and creating custom properties for them. This activity led to us thinking about what those properties can communicate and to who they will communicate so we made a game which fleshes out on that idea of properties communicating information.

## What it does
This is a 3D sandbox survival game where the user creates a base out of various objects (Speckle objects imported and tied to sprites in Unity). These objects each have their own properties determined by the materials that they are made out of. For example, wood walls are strong but flammable, concrete walls are strong but heavy, a wood door is weak and flammable and a reinforced concrete roof is very heavy. Once the user places their objects down and makes their house the entire model is sent to Speckle for some behind the scenes magic. A Speckle Automate program takes in the model and runs calculations for building integrity and weaknesses based on our own rules. It returns weak points and points like pillars which are important for structural integrity and returns this to the enemy AI. The enemies then take this information and target the points of weakness based on their own strengths. For example, a fire enemy would target the wood parts to burn them and create entry. A strong enemy would go and target the pillars in order to take out the structural support. The round is ended either when the house is destroyed or the enemies are eliminated. After it is done the model is once again sent to a speckle automate script where the user is sent a list of repairs to do and the cycle starts again.

## How we built it
We built this project in Unity, splitting the tasks evenly based on individual skills. Angela worked on the enemy AI, Andrew worked on the game scripting and Tyler worked on the automate scripts. 

## Challenges we ran into
We ran into a lot of challenges when taking on this project. The idea overall was too much for only a weekend so we didn't get to connect or polish the three parts. Overall the biggest issue we faced was a lack of knowledge on how to use Unity. I think we were a little overambitious for how much we could learn in a weekend so we were not able to make our vision come to life in a really satisfying way. 

## Accomplishments that we're proud of
We were able to create parts of the whole which we are proud of. Our enemy AI is somewhat basic but it targets objects in the way that we want them to and that was exciting to see work. Also, the game itself is functional. There is a system for placing objects and removing them and even if this was not connected to the enemy AI due to time constraints, this was a nice thing to see come to life. 

## What we learned
We all learned a lot about learning other languages and platforms. Unity is something which we are all much more familiar with and along with that came some gained fluency in C# which is a great thing to know. We also learned a little more about realistic goal setting. It's important to take a step back when creating an idea for a project and ask if it is really possible to do in the time frame. 

## What's next for Speckle Survival
We would love to see it fully functional. The next steps would be to finish the automation functions and tie them into the game along with the enemy AI. The final goal is to have the game we imagine be playable even if it is rough and unpolished. We would just love to see the gameplay loop up and functional.
