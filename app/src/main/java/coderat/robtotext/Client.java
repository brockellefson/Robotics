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

    public Client(String inIP, int inPort){
        ip = inIP;
        port = inPort;
    }

    public void send(String message){
        try {
            client = new Socket(ip, port);
            System.out.println("Client connected to ROB");
            DataOutputStream out = new DataOutputStream(client.getOutputStream());
            out.writeUTF(message);
            System.out.println("Sent Message: " + message);
            out.close();
            client.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }


    @Override
    public void run() {
        System.out.println("Client Thread Starting");
        Looper.prepare();
          handler = new Handler() {
                public void handleMessage(Message msg){
                    String response = msg.getData().getString("CM");
                    send(response);
                }
            };
        Looper.loop();
    }
}
