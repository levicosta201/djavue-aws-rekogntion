import axios from '~/helpers/axios';

axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.xsrfCookieName = "csrftoken";

const api = {
    login(username, password){
        return post('/api/login', {username: username, password: password});
    },
    logout(){
        return post('/api/logout');
    },
    whoami(){
        return get('/api/whoami');
    },
    add_todo(newtask){
        return post('/api/add_todo', {new_task: newtask});
    },
    list_todos(){
        return get('/api/list_todos');
    },
    list_clients(){
        return get('/api/list_clients');
    },
    validate_client(client){
        return post('/api/validate_client', {client_id: client.selected, client_photo:client.photo}, {
            headers: {
                'content-type': 'multipart/form-data'
            }
        });
    },
    register_client(client){
        return post('/api/add_client', {firstname: client.firstname, lastname:client.lastname, email:client.email, document:client.document}, {
            headers: {
                'content-type': 'multipart/form-data'
            }
        });
    }
}
export default api;

function get(url, params){
    return axios.get(url, {params: params});
}

function post(url, params, config){
    var fd = new FormData();
    params = params || {}
    Object.keys(params).map((k) => {
        fd.append(k, params[k]);
    })
    return axios.post(url, fd, config);
}
