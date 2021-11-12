import React, {useState} from 'react';
import { useParams } from "react-router-dom";
import axios from 'axios';

import Button from '@mui/material/Button';
import Rating from '@mui/material/Rating';

import './customer.css';
import API_BASE_URL from '../config';

interface ParamTypes {
    username: string,
    order_id: string
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
    
    const [orderTime, setOrderTime] = useState("press button to update");
    const [ETA, setETA] = useState("press button to update");

    function buttonHandler() {
        let payload = {
            username: username,
            order_id: order_id,
        };
        
        let orderTime: string, eta: string;
        axios.request({
            method: 'post',
            url: API_BASE_URL + "/api/getOrder",
            data: payload,
        })
        .then(res => { 
            console.log(res)
            orderTime = res.data.orderTime;
            eta = res.data.eta;

            setOrderTime(prev => orderTime);
            setETA(prev => eta);
        })
    }


    function ratingHandler(ratingVal: number | null) {
        let payload = {
            username: username,
            order_id: order_id,
            rating: ratingVal
        }

        axios.request({
            method: "post",
            url: API_BASE_URL + "/api/postRating",
            data: payload
        }).then(res => {
            console.log(res);
        })
    }


    return (
        <div className="customer">
            <h1>Hello {username}, this page is for your order with ID: {order_id}</h1>
            <p>order placed at: { orderTime } </p>
            <p>ETA: { ETA }</p>

            <Button variant="contained"
                onClick={() => buttonHandler()}>Click to Update Order Status</Button>


            <p>==========</p>

            <p>Please input your rating for this meal:</p>
            <Rating
                name="simple-controlled"
                defaultValue={0.0}
                onChange={(event, newValue) => {
                    ratingHandler(newValue);
                    alert("rating posted successfully!");
                }}
            />

        </div>
    )

    
}


export default function customer() {
    return <CustomerContent />;
}
