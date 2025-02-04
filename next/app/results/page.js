"use client"
import { useEffect } from "react"

const ResultsPage = () => {
    useEffect(()=>{
        const loadResults = async()=>{
            const res = await fetch("http://localhost:8000/results")
            const data = await res.json()
            console.log(data)
        }
      loadResults()  
    }, [])
    return("OIFKHDSOIFHAjsdoikf")
}

export default ResultsPage