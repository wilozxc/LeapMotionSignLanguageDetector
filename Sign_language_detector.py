import sys,os
import Leap,time,math,time

fing1 = 0
fing2 = 0
fing3 = 0
fing4 = 0
fing5 = 0

def on_frame ():
    while True:
        controller = Leap.Controller()
        f = controller.frame()
        hand = f.hands.rightmost

        pinch = hand.pinch_strength           
        strength = hand.grab_strength
        hand_direction = hand.direction
        fps = f.current_frames_per_second
        frame_identifier = math.floor(f.id)
        hand_identifier = hand.id
        
##        fr1=int(frame_identifier)
##        fr2 = int(frame_identifier)
##        fr1 +=1
##        print frame_identifier,fr1
##
##        
##        
##        while fr1 == fr2:
##                print "ya",
##                fr2 = int(frame_identifier)
##            
##        fr2 = int(frame_identifier)
##        print 'no'
 
            
        hand_name = "Left hand" if hand.is_left else "Right hand"
        
        #print len(f.fingers.extended()),strength,pinch

        
        if strength == 1 :
            a = 'fist'
            os.system("say %s" % a)
            print a
            time.sleep(1)

        if len(f.fingers.extended()) == 1 and pinch > 0.5:
            a= '1'
            os.system("say %s" % a)
            print a
            time.sleep(1)

        if len(f.fingers.extended()) == 2 and pinch > 0.5:
            a= '2'
            os.system("say %s" % a)
            print a
            time.sleep(1)

        if len(f.fingers.extended()) == 3 and  0.9 > pinch > 0.5 :
            a= '3'
            os.system("say %s" % a)
            print a
            time.sleep(1)

        if len(f.fingers.extended()) == 4 and pinch == 0 and strength == 0:
            a= '4'
            os.system("say %s" % a)
            print a
            time.sleep(1)

        if len(f.fingers.extended()) == 5 and pinch == 0 and strength == 0:
            a= '5'
            os.system("say %s" % a)
            print a
            time.sleep(1)

        if len(f.fingers.extended()) == 3  and pinch == 1 and strength == 0:
            a= '6'
            os.system("say %s" % a)
            print a
            time.sleep(1)

        

 

        

 

     
                
            
on_frame()

    
 
