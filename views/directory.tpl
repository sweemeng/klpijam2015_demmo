<html>
  <head><title>Just a image dir</title></head>
  <body>
    % for item in directory:
      <img src="/static/{{item}}"/><br/>
    % end
  </body>
</html>
