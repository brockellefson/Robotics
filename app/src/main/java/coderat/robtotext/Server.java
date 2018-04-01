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

    public Server(int inPort){
        port = inPort;
    }

    public void processResponse(String response){
        //not sure how to process this yet
    }

    public void runServer(){
        try{
            server = new ServerSocket(port);
            while(true){
                Socket socket = server.accept();
                BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                String response = in.readLine();
                in.close();
                socket.close();

                if(response != null){
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
        runServer();
    }
}
