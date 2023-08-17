import React, {useState, createContext, useContext, useEffect} from "react"

export const ContextStore = createContext(null)
export default ({children}) => {
    console.log("Hello world!!")

    const [userDict, setUserDict] = useState([])

    useEffect(() => {
        fetchProfiles();
    }, []);

    const fetchProfiles = async () => {
        const response = await fetch('http://localhost:8000/profiles/')
        console.log(response)
        if (response.ok) {
            const data = await response.json();
            setUserDict(data.profile);
        }
    };
    
    console.log(userDict)

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