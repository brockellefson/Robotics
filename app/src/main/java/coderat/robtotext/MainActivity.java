package coderat.robtotext;

import android.content.ActivityNotFoundException;
import android.content.Intent;
import android.os.Message;
import android.speech.RecognizerIntent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageButton;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.Locale;

public class MainActivity extends AppCompatActivity {

    //interface buttons
    private TextView input;
    private ImageButton speakButton;
    private ImageButton sendButton;
    private ImageButton conButton;

    //networking
    private Client client;
    private String message;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //create ref to buttons
        speakButton = findViewById(R.id.speakbutton);
        sendButton = findViewById(R.id.sendbutton);
        conButton = findViewById((R.id.wififragbutton));
        input = findViewById(R.id.speechtext);

        //create network
        client = new Client("localhost", 3030);
        Thread clientThread = new Thread(client);
        clientThread.start();

        //create a listener for the send button
        sendButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {SendTTS();
            }
        });


        //create a listener for the speech button
        speakButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {SpeechInput();
            }
        });

    }

    //speech listener
    private void SpeechInput() {
        Intent intent = new Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH);
        intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM);
        intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, Locale.getDefault());
        intent.putExtra(RecognizerIntent.EXTRA_PROMPT, "ay boi lets hit it");
        try {
            startActivityForResult(intent, 100);
        } catch (ActivityNotFoundException e) {

        }
    }

    //send the tts create message to the py
    private void SendTTS(){
        if(message != null){
            Message clientMsg = client.handler.obtainMessage();
            Bundle b = new Bundle();
            b.putString("CM", message);
            clientMsg.setData(b);
            client.handler.sendMessage(clientMsg);
        }
    }


    //display text from speech
    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        switch (requestCode) {
            case 100: {
                if (resultCode == RESULT_OK && null != data) {
                    ArrayList<String> result = data.getStringArrayListExtra(RecognizerIntent.EXTRA_RESULTS);
                    input.setText(result.get(0));
                    message = result.get(0);
                }
                break;
            }

        }
    }


}