import Axios from 'axios';

const baseURL = "http://localhost:5000";
const axios = Axios.create({
    baseURL
})

export default axios