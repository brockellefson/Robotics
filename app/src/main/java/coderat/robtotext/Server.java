package coderat.robtotext;

import android.os.Bundle;
import android.os.Message;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;

/**
 * Created by Brock on 3/31/2018.
 */

public class Server implements Runnable{
    private int port;
    private ServerSocket server;
    private TTS tts;

    public Server(int inPort, TTS inTTS){
        port = inPort;
        tts = inTTS;
    }

    //process response and translate it to speech
    public void processResponse(String response){
        Message ttsMsg = tts.handler.obtainMessage();
        Bundle b = new Bundle();
        b.putString("TT", response);
        ttsMsg.setData(b);
        tts.handler.sendMessage(ttsMsg);
    }

    //listen for any incoming messages from rob
    public void runServer(){
        try{
            System.out.println("Starting up server...");
            server = new ServerSocket(port);
            while(true){
                Socket socket = server.accept();
                BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                String response = in.readLine();
                in.close();
                socket.close();

                if(response != null){
                    System.out.println("INCOMING MESSAGE: " + response);
                    processResponse(response);
                    response = null;
                }

            }
        } catch (IOException e) {
            //ouch lol
        } catch (Exception e) {
            //eek lol
        }
    }

    @Override
    public void run() {
        System.out.println("Server Thread Starting");
        runServer();
    }
}
