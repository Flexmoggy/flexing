import React, {useState, createContext, useContext} from "react"

export const ContextStore = createContext(null)
export default ({children}) => {
    // console.log("Hello World!")

    const [count, setcount] = useState(0)

    const store = {
        count: count,
        setcount: setcount,
    }
    return <ContextStore.Provider value={store}>{children}</ContextStore.Provider>
}

export const useContextStore = () => useContext(ContextStore)
