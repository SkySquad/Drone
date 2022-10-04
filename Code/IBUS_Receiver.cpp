#include <Arduino.h>

#include "IBUS_Receiver.h"
#include "FlySkyIBus_Decoder.h"

IBus_Receiver::IBus_Receiver(){
<<<<<<< HEAD
    for(int i=0; i<nr_of_channels; i++){
        channels[i].setChannelNr(i);
    }

    Serial.begin(115200);
    IBus.begin(Serial);
}

Channels1to4_read IBus_Receiver::readChannels1to4(void){
    IBus.loop();

    Channels1to4_read temp;
    for(int i=0; i<4; i++){
        temp.arr[i] = channels[i].readValue();
    }
    return temp;
}

int IBus_Receiver::readChannel6(void){
    IBus.loop();
    return channels[5].readValue();
}


Channel::Channel(){
}

int Channel::readValue(void){
    value = IBus.readChannel(channelNr);
    return value;
}

void Channel::setChannelNr(int x){
    channelNr = x;
}
=======
    Serial.begin(115200);
    FlySkyIBus.begin(Serial);
}

void IBus_Receiver::readChannels1to4(void){

}

void IBus_Receiver::readChannel6(void){

}


class Channel{
    private:
        int read;
        int channelNr;
    public:
        Channel();
        int readValue(void);
        void setChannelNr(int x);
}

int Channel::readValue(void){
    self.read = FlySkyIBus.readChannel(self.channelNr);
}

void Channel::setChannelNr(int x){
    self.channelNr = x;
}

IBus_Receiver IBus_Receiver_Drone = IBUS_Receiver();
>>>>>>> 3516017 (mod README and rebasing)
