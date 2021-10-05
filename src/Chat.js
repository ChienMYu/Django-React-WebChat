import React, {useEffect, useState} from 'react';
import { w3cwebsocket as W3CWebSocket } from 'websocket';

const client = new W3CWebSocket('ws://127.0.0.1:8000/ws/chat/test/');

export default function Chat() {

    const [msgs, setMsgs] = useState(()=>{return []})

    const sendMessage = () => {
        const msg = document.querySelector('#text')
        client.send(JSON.stringify({
            type: "message",
            message: msg.value
        }));
        msg.value = ''
    }

    const getTen = async () => {
        const res = await fetch('http://127.0.0.1:8000/messages/load/ten/')
        const data = await res.json()
        let tenMsgs = []
        for(let obj of data){
            tenMsgs.push(obj.content)
        }
        setMsgs(tenMsgs)
    }
    useEffect(() => {
        getTen()
    },[])


    useEffect(()=>{
        client.onopen = () => {console.log("Web Socket Client connected")}
        client.onmessage= (message) => {
            const data = JSON.parse(message.data)
            console.log("Got reply!", data)
            setMsgs((msgs) => [...msgs, data.message])
        }
        client.onclose = (e) => {console.error("Chat socket closed unexpectedly!")}

        return () => client.close()
    }, [])



    return (
        <div>
            Chat is connected
            <div id='chat-log'>
                {msgs.map((m,i)=><p key={i}>{m}</p>)}
            </div>
            <input id='text' type='text'/>
            <button onClick={()=>sendMessage()}>Click Me</button>
        </div>
    )
}
