
<rspec xmlns:client="http://www.protogeni.net/resources/rspec/ext/client/1" xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" xmlns:jacks="http://www.protogeni.net/resources/rspec/ext/jacks/1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.geni.net/resources/rspec/3" xsi:schemaLocation="http://www.geni.net/resources/rspec/3 http://www.geni.net/resources/rspec/3/request.xsd" type="request">
  <rspec_tour xmlns="http://www.protogeni.net/resources/rspec/ext/apt-tour/1">
    <description type="text">This profile provides a baseline Ubuntu 14.4 image</description>
  </rspec_tour>
  <node client_id="basenode" exclusive="true">
    <sliver_type name="raw">
      <disk_image name="urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU14-64-STD"/>
    </sliver_type>
    <services>
      <execute shell="/bin/sh" command="touch test.txt"/>
    </services>
  </node>
</rspec>
