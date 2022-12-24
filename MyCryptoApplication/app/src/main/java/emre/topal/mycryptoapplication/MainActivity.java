package emre.topal.mycryptoapplication;

import static android.widget.Toast.makeText;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.os.SystemClock;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.firebase.firestore.DocumentReference;
import com.google.firebase.firestore.DocumentSnapshot;
import com.google.firebase.firestore.EventListener;
import com.google.firebase.firestore.FirebaseFirestore;
import com.google.firebase.firestore.FirebaseFirestoreException;
import com.google.firebase.firestore.QuerySnapshot;

import java.util.HashMap;

import emre.topal.mycryptoapplication.databinding.ActivityMainBinding;

public class MainActivity extends AppCompatActivity {

    private Button btnKayit;
    private EditText editText;
    private ActivityMainBinding binding;
    private FirebaseFirestore firestore;
    private String deneme;
    private Deneme sinif;
    private TextView tahmin;
    private Button infoBtn;
    String id;


    public MainActivity(){

    }



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        firestore = FirebaseFirestore.getInstance();
        editText = findViewById(R.id.editTextTextPersonName);
        btnKayit = findViewById(R.id.button);
        tahmin = findViewById(R.id.txtTahmin);
        infoBtn = findViewById(R.id.infoBtn);


        btnKayit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                saveNews();

            }



        });


        infoBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent goToInfoActivity = new Intent(getApplicationContext(), InfoActivity.class);
                startActivity(goToInfoActivity);
            }
        });











    }

    private void saveNews() {

        if(editText.getText().equals("")){
            Toast.makeText(this,"ben çalışıyorum ",Toast.LENGTH_LONG).show();
        }{
            HashMap<String,Object> data = new HashMap<>();
            data.put("haber",editText.getText().toString());
            data.put("durum","empty");
            firestore.collection("BTCHABER").add(data).addOnSuccessListener(documentReference -> {
                id = documentReference.getId();
                SystemClock.sleep(3000);
                makeText(this,"işlem tamamlandı",Toast.LENGTH_LONG).show();

                sinif =new  Deneme();
                firestore.collection("BTCHABER").addSnapshotListener((value, error) -> {
                    if (value.isEmpty()){

                    }else {
                        for(DocumentSnapshot document: value.getDocuments()){
                            if(document.getId().equals(id)){
                                tahmin.setText(document.get("durum").toString());
                               // System.out.println(document.get("durum").toString());
                            }

                        }
                    }
                });

                SystemClock.sleep(2000);



            }).addOnFailureListener(e -> {
                 makeText(this,e.getLocalizedMessage(),Toast.LENGTH_LONG).show();
            });


        }
    }


    public void deneme(View view){
        makeText(this,"Merhabalar ",Toast.LENGTH_LONG).show();
    }

    public void don(){








    }
}