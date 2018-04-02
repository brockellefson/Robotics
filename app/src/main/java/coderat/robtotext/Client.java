package coderat.robtotext;

import android.os.Handler;
import android.os.Looper;
import android.os.Message;

import java.io.DataOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.net.Socket;

/**
 * Created by Brock on 3/31/2018.
 */

public class Client implements Runnable{
    private String ip;
    private int port;
    private Socket client;
    public Handler handler;
    private String message;

    public Client(String inIP, int inPort, String inMessage){
        ip = inIP;
        port = inPort;
        message = inMessage;
    }

    public void send(String message){
        try {
            client = new Socket(ip, port);
            System.out.println("Client connected to ROB");
            OutputStream outToServer = client.getOutputStream();
            DataOutputStream out = new DataOutputStream(outToServer);
            out.writeUTF(message);
            System.out.println("Sent Message: " + message);
            client.close();
        } catch (IOException e) {
            //ouch lol
            e.printStackTrace();
        } catch (Exception e) {
            //eek lol
            e.printStackTrace();
        }
    }


    @Override
    public void run() {
        System.out.println("Client Thread Starting");
        send(message);
    }
}
