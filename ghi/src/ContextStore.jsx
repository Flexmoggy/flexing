import React, {useState, createContext, useContext} from "react"

export const ContextStore = createContext(null)
export default ({children}) => {

    const [userDict, setUserDict] = useState({
        first_name: "A",
        last_name: "Aron",
        skills: "Sleeping",
        interests: "Eating",
        bio: "Prow?? ew dog you drink from the toilet, yum yum warm milk hotter pls, ouch too hot open the door, let me out, let me out, let me-out, let me-aow, let meaow, meaow! yet mess up all the toilet paper scoot butt on the rug so attack feet grass smells good so hit you unexpectedly. Miaow then turn around and show you my bum pet my belly, you know you want to; seize the hand and shred it!. Sniff sniff stuff and things for pet my belly, you know you want to; seize the hand and shred it!. Run at 3am lie in the sink all day going to catch the red dot today going to catch the red dot today kitty ipsum dolor sit amet,"
    })

    const [count, setcount] = useState(0)

    const store = {
        count: count,
        setcount: setcount,
        userDict: userDict,
        setUserDict: setUserDict
    }
    return <ContextStore.Provider value={store}>{children}</ContextStore.Provider> 
}

export const useContextStore = () => useContext(ContextStore)