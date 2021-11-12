import React, {useState} from 'react';
import { useParams } from "react-router-dom";
import axios from 'axios';

import Button from '@mui/material/Button';

interface ParamTypes {
    username: string,
    order_id: string
}

interface headerTypes {
    'Content-Type': string,
    'Access-Control-Allow-Origin': string,
}

// interface Props {
// }

function CustomerContent() {
    // constructor(props: Props) {
    //     super(props);

        
    // }

    let {username, order_id} = useParams<ParamTypes>();
        console.log(username);
        console.log("hi");
    
    const [orderTime, setOrderTime] = useState(0);
    const [ETA, setETA] = useState(0);

    function buttonHandler() {
        let payload = {
            username: username,
            order_id: order_id,
        };

        axios.request<ParamTypes, string>({
            method: 'post',
            url: 'http://localhost:5000/api/test',
            data: payload
        })
        .then(res => { 
            console.log(res)
        })
              
        setOrderTime(prev => prev + 1);
        setETA(prev => prev + 1);
    }

    return (
        <div>
            <h1>Hello {username}, this page is for your order with ID: {order_id}</h1>
            <p>order placed at: { orderTime } </p>
            <p>ETA: { ETA }</p>

            <Button variant="contained"
                onClick={() => buttonHandler()}>Click to Update Order Status</Button>

        </div>
    )

    
}


export default function customer() {
    return <CustomerContent />;
}
