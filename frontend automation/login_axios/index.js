const axios = require('axios').default;

const cookies = {}

const session = axios.create();
session.defaults.withCredentials = true;
session.defaults.headers['user-agent'] = 'Chromium/51.0.2704.63';

function parseCookies(response) {
    const setCookies = response.headers['set-cookie'];
    for (const cookie of setCookies) {
        const pair = cookie.split(';')[0].split('=');
        cookies[pair[0]] = pair[1];
    }

    let cookieString = '';
    for (const key of Object.keys(cookies)) {
        cookieString += `${key}=${cookies[key]}; `;
    }
    session.defaults.headers['Cookie'] = cookieString.trim();
    
}

async function main() {
    // const baseURL = 'https://clashofcodes.herokuapp.com/signin';
    const loginURL = 'https://clashofcodes.herokuapp.com/user/signin';
    // const initialRequest = await session.get(baseURL);
    // console.log(initialRequest.headers)
    // parseCookies(initialRequest);
    // console.log(cookies);
    // console.log(session.defaults.headers);
    loginCheckPayload = '{"email":"ahlawataman3@gmail.com","password":"temporarypass"}';
    const loginCheck = await session.get(loginURL, loginCheckPayload);
    console.log(loginCheck.headers);
}

main();