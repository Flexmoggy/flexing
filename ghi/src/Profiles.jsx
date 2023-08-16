import React, { useState, useEffect } from 'react';
import {useContextStore} from './ContextStore';
import ProfileCard from './ProfileCard'

/* <h2>
    <button onClick={() => setcount(count+1)}>Add a profile</button>
  </h2> */
 
function Profiles() {

const [profiles] = useState([
  {
  userName: "A",
  skills: "Sleeping",
  interests: "Eating",
  bio: "Prow?? ew dog you drink from the toilet, yum yum warm milk hotter pls, ouch too hot open the door, let me out, let me out, let me-out, let me-aow, let meaow, meaow! yet mess up all the toilet paper scoot butt on the rug so attack feet grass smells good so hit you unexpectedly. Miaow then turn around and show you my bum pet my belly, you know you want to; seize the hand and shred it!. Sniff sniff stuff and things for pet my belly, you know you want to; seize the hand and shred it!. Run at 3am lie in the sink all day going to catch the red dot today going to catch the red dot today kitty ipsum dolor sit amet,"
  },
  {
  userName: "B",
  skills: "Napping",
  interests: "Scarfing",
  bio: "hed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff. Toy mouse squeak roll over flee in terror at cucumber discovered on floor steal mom's crouton while she is in the bathroom soft kitty warm kitty little ball of furr yet i'm bored inside, let me out i'm lonely outside, let me in i can't make up my mind whether to go in or out, guess i'll j"
  },
    {
  userName: "C",
  skills: "Binging netflix",
  interests: "Snowboarding",
  bio: "Step on your keyboard while you're gaming and then turn in a circle favor packaging over toy and hey! you there, with the hands scratch at fleas, meow until belly rubs, hide behind curtain when vacuum cleaner is on scratch strangers and poo on owners food yet meow loudly just to annoy owners. Claws in your leg dream about hunting birds cats are the world jump on fridge leave buried treasure in the sandbox for the toddlers. Drool be a nyan cat, feel great about it, be annoying 24/7 poop rainbows in litter box all day so inspect anything brought into the house. Kitty pounce, trip, faceplant you didn't see that no you didn't definitely didn't lick, lick, lick, and preen away the embarrassment human clearly uses close to one life a night no one naps that long so i revive by standing on chestawaken!"
  },
    {
  userName: "D",
  skills: "Napping",
  interests: "Yawning",
  bio: "Even more stuff!"
  },
    {
  userName: "E",
  skills: "Snoozing",
  interests: "Juggling",
  bio: "Even more stuff!"
  },
    {
  userName: "F",
  skills: "Cross-country skiing",
  interests: "None",
  bio: "Even more stuff!"
  }
]);

console.log(profiles)
  return (
    <div>
      <h1>Profiles</h1>
      <div>
        {profiles.map((profile, index) => {
          if (index % 3 === 0)
            return (
              <div className="row mb-4">
                <div className="col-4 h-5">
                  <div className="card mh-100 bg-info border-dark" style={{width: '33', height: '500px'}}>
                    <div className="card-body overflow-auto">
                      <h1>{profiles[index].userName}</h1>
                      <h2>{profiles[index].skills}</h2>
                      <p>{profiles[index].skills}</p>
                      <h2>Interests</h2>
                      <p>{profiles[index].interests}</p>
                      <h2>Bio</h2>
                      <p>{profiles[index].bio}</p>
                    </div>
                  </div>
                </div>
                <div className="col-4">
                  <div className="card mh-100 bg-info border-dark" style={{width: '33', height: '500px'}}> 
                    <div className="card-body overflow-auto">
                      <h1>{profiles[index+1].userName}</h1>
                      <h2>{profiles[index+1].skills}</h2>
                      <p>{profiles[index+1].skills}</p>
                      <h2>Interests</h2>
                      <p>{profiles[index+1].interests}</p>
                      <h2>Bio</h2>
                      <p>{profiles[index+1].bio}</p>
                    </div>
                  </div>
                </div>
                <div className="col-4">
                  <div className="card mh-100 bg-info border-dark" style={{width: '33', height: '500px'}}>
                    <div className="card-body overflow-auto">
                      <h1>{profiles[index+2].userName}</h1>
                      <h2>{profiles[index+2].skills}</h2>
                      <p>{profiles[index+2].skills}</p>
                      <h2>Interests</h2>
                      <p>{profiles[index+2].interests}</p>
                      <h2>Bio</h2>
                      <p>{profiles[index+2].bio}</p>
                    </div>
                  </div>
                </div>
              </div>
            )
        })}
      </div>
    </div>
  );
}

export default Profiles;

