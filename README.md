# auto-chat-facebook
auto message send in facebook using python fbchat module


<i> when using this script there will be a error like </i> <b>list index out of range</b> 

<h3> solution: </h3>

    Change

    revision = int(r.text.split('"client_revision":', 1)[1].split(",", 1)[0])

    to

    revision = 1


There is three kind of script:

  1. deafult 
  2. session
  3. session generator
  
<p> deafult works by just username and password , and it works fine , but when you will try to use it in a remote server it will throw many errors.
beacuse of facebook tracks the login location thats why login from unknown location will be blocked. <p>

To bypass this issue we have <b> session handeling  </b> 
  <div> 
      to use it you will have to run the session generator on your computer and it will output a session.json file  
      then you will have to put the session.json file in your remote server , after that it will run perfectly . 
      Beacuse you are providing the session of your local computer facebook will think the remote server as your local computer and it will allow to access facebook.
  </div>
  
  

