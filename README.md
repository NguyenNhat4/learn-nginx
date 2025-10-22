# How-to Guide


1. Install the `htpasswd` utility
    ```shell
    sudo apt-get install apache2-utils
    ```
2. Create the password file
    ```shell
    cd nginx
    sudo htpasswd -c .htpasswd your_username
    ```
    Please feel free to change `your_username` by providing your own. Now you should see the password file `.htpasswd` was updated with the new configuration.

## Load balancing
When you make a request to the path `/service1`, NGINX will handle load balancing the request to either `/nginx-tutorials-api-1-1` or `nginx-tutorials-api-1-2` according to the NGINX configuration below.

```
upstream api_service_1 {
    server nginx-tutorials-api-1-1:30000;
    server nginx-tutorials-api-1-2:30000;
}
```
