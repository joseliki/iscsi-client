<<<<<<< HEAD
iscsi-client
============

repositorio sobre cliente iscsi
=======
<<<<<<< HEAD
Bottle on OpenShift
===================

This git repository helps you get up and running quickly w/ a Bottle installation
on the Red Hat OpenShift PaaS.


Running on OpenShift
----------------------------

Create an account at https://www.openshift.com/

Create a python application

    rhc app create bottle python-2.6

Add this upstream bottle repo

    cd bottle
    git remote add upstream -m master git://github.com/openshift-quickstart/bottle-openshift-quickstart.git
    git pull -s recursive -X theirs upstream master
    
Then push the repo upstream

    git push

That's it, you can now checkout your application at:

    http://bottle-$yournamespace.rhcloud.com

=======
python-bottle
=============

repositorio de prueba sobre python bottle
>>>>>>> 311744ed19344bb3893698ea8c63e19535b3f2a1
>>>>>>> 40d56bf941906dd8ce55c9b7c221835498cd9952
