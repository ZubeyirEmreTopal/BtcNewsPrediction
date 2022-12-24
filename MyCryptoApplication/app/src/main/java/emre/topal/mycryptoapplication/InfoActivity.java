package emre.topal.mycryptoapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.text.method.ScrollingMovementMethod;
import android.widget.TextView;

public class InfoActivity extends AppCompatActivity {
    private TextView klavuztxt;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_info);
        klavuztxt=findViewById(R.id.klavuztxt);
        klavuztxt.setMovementMethod(new ScrollingMovementMethod());
    }
}