# jinkies
# What is this project?
I want to self-host a build system that can make my projects straight from my github repos. 
I want it to be an open source option for hobbyists who don't want to learn github actions, circleci yaml or
anything else. Instead, it's for people who want to run a Jenkinsfile on a Jenkins server, a build system
which has already stood the test of time.

# Why is this project?
I have ideas for simple, small, hobbyist tools, and this is one of those ideas.

# How do I get started using this project?
It's all in dev mode, so  check out the Docker directory and use the build_image script to build the container and the jinkies script to run the container.

# Design
Jinkies is designed to be a flexible, extensible Jenkins base. We want to offer flexible configuration of every piece of Jenkins that we interact with, to
allow end users maximum extensibility as well as being a firm foundation for people to learn about Jenkins from.

## How to customise configuration files
Where possible, configuration files are read from files pointed to by environment variables. This allows this project to ship a sane default jinkies system,
while also allowing consumers of the project to provider their own version of the file by mounting in the file and overriding the contents of the environment.

These environment variables will be called JINKIES_$FEATURE and are documented in Docker/build.env


## Seed Job Implementation
The seed job implementation can be provided as a Jenkinsfile. Provide The seed job hook script evaluates an environment variable



                                                                                                    
                                                        `:/oys+-                                    
                                                     .:ossyddmmddo.                                 
                                                  `:ossssymmmmmmmmdy+                               
                                                  +ssssssshmmmmmmdmms                               
                                                  yyyysssysyyddmmmmmms`                             
                                                  `ommhshydhmhdhdmmmmms                             
                                                   /Nydym//+Noohdmmmmmh                             
                                                `.ohmyy:ssshy/yddmmmmh.                             
                                               .oydmh-/+/:-:+hmdmmdh+`                              
                                                 ./yhs::d+-ohhdmdd/`                                
                                                    /syoo+s+oyyhss`                                 
                                                    :osssososyoyss                                  
                                                   `.soo//s+sysyhs`                                 
                                                  .++ooo/+soo+//++`                                 
                                               ``/s///+++//////+oss`                                
                                             :/++/////////////+ooooo                                
                                            ///////////////+++ooooso                                
                                            -s////////////+o+ooooss`                                
                                         .-:ysy///+s/////+o/oooos+                                  
                                         :ys+/y/////o+//os/oooso-                                   
                                        :++s-:s//////+osyyyoosh`                                    
                                        oosy/:/++++++hsyhhyssho                                     
                                        ohhos/++::+oooysshyssh/                                     
                                        `:+ss:ysyoy++oyoossssh:                                     
                                           ` `yooohssshsossysso`                                    
                                              s///+ysssssysoooss:                                   
                                              o//////////+oooooos+`                                 
                                              +///////////+ooooooss.                                
                                              -o///////////+ooooossy`                               
                                               o////////////+oosyhddy-                              
                                               +s+/////////++shddddddds.                            
                                              -yddhysssyyhhhddmddddmddddo`                          
                                             :hhdyhhdhhhhdddddddddddmddh/                           
                                            :hhdyyyhhyyyyddddddmdddddd+`                            
                                            `/yhyyydyyyyyhddddddddyo:`                              
                                              /+osydyyyyyymdddhys-                                  
                                              +-:::/++yoooo+/:::+                                   
                                            `/-..-:::/+o:::::::o.                                   
                                            :/..-:://. `+...-::o`                                   
                                           `+:..:://    /-.-o::/+                                   
                                           +o/://///     +--::::+/                                  
                                          :+//+ooss:     o/:++ooso                                  
                                         .so++oooss`     +//ossos:                                  
                                        `o//ossys/`      +//oosso                                   
                                        +//ooso/.        :o+sssy.                                   
                                       /+/oso/`          `o/oos/                                    
                                      :++oo:`             s/oos`                                    
                          `o/-.````../++s:`               s+os-                                     
                          `ohdysyyys++oy-                 s+so                                      
                            .+yhhhhdhhhs                 -+os/                                      
                              `..-:hhho.                -yossy                                      
                                   .-`                `+hhdddd`                                     
                           ::-::                    `:oyddmdh/                                      
                           --.``                   :shyhdh:-`                                       
                          `-....`` `              -yhhyo/`
