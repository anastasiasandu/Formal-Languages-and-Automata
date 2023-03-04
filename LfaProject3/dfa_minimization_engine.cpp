#include <fstream>
#include <iostream>
#include <cstring>

using namespace std;
ifstream fin("dfa_config_file");
int main()
{
    char s[300];
    int nr=0,lungimeSigma=0,lungimeStates=0,lungimeTransitions=0;
    string sigma[100],states[100],transitions[100];
    string p;
    char *q;
    int n=0;
    bool tipStates[100];
    while(nr<3)
    {
        fin.getline(s,300);
        if(strcmp(s,"End")==0)
            nr++;
        if(s[0]!='#')
        {
            if (strstr(s,"Sigma")==s)
            {
                fin.getline(s,300);
                while(s[0]=='#')
                    fin.getline(s,300);
                while (strcmp(s,"End")!=0)
                {

                    while(s[0]=='#')
                        fin.getline(s,300);
                    p="";
                    for(int i=0; s[i]; i++)
                    {
                        if(s[i]=='#' || s[i]==' ')
                            break;
                        p+=s[i];
                    }

                    sigma[lungimeSigma]=p;
                    lungimeSigma++;
                    fin.getline(s,300);
                }
                nr++;
            }
            else if(strstr(s,"States")==s)
            {
                fin.getline(s,300);
                while(s[0]=='#')
                    fin.getline(s,300);
                while (strcmp(s,"End")!=0)
                {

                    while(s[0]=='#')
                        fin.getline(s,300);
                    q=strtok(s,",");
                    while(q)
                    {

                        p="";
                        for(int i=0; q[i]; i++)
                        {
                            if(q[i]=='#' || q[i]==' ')
                                break;
                            p+=q[i];
                        }

                        states[lungimeStates]=p;
                        lungimeStates++;
                        q=strtok(0,",");
                    }
                    fin.getline(s,300);
                }
                nr++;
            }
            else if(strstr(s,"Transitions")==s)
            {

                fin.getline(s,300);
                while(s[0]=='#')
                    fin.getline(s,300);
                while (strcmp(s,"End")!=0)
                {

                    while(s[0]=='#')
                        fin.getline(s,300);
                    q=strtok(s,",");
                    while(q)
                    {

                        p="";
                        for(int i=0; q[i]; i++)
                        {
                            if(q[i]=='#' || q[i]==' ')
                                break;
                            p+=q[i];
                        }

                        transitions[lungimeTransitions]=p;
                        lungimeTransitions++;
                        q=strtok(0,",");
                    }
                    fin.getline(s,300);
                }
                nr++;
            }
        }
    }
    /*
    cout<<"sigma: "<<endl;
    for(int i=0; i<lungimeSigma; i++)
        cout<<sigma[i]<<endl;
    cout<<"states: "<<endl;
    for(int i=0; i<lungimeStates; i++)
        cout<<states[i]<<endl;
    cout<<"trans: "<<endl;
    for(int i=0; i<lungimeTransitions; i++)
        cout<<transitions[i]<<endl;
    */
    string start;
    for(int i=0; i<lungimeStates-1; i++)
        if(states[i]!="F" && states[i]!="S" && states[i+1]!="F" && states[i+1]!="S")
            tipStates[n++]=0;
        else if(states[i]!="F" && states[i]!="S" && states[i+1]=="F")
        {
            for(int k=i+1; k<lungimeStates-1; k++)
                states[k]=states[k+1];
            lungimeStates--;
            tipStates[n++]=1;
        }
        else if(states[i]!="F" && states[i]!="S" && states[i+1]=="S")
        {
            start = states[i];
            for(int k=i+1; k<lungimeStates-1; k++)
                states[k]=states[k+1];
            lungimeStates--;
            tipStates[n++]=0;
        }
    if(states[lungimeStates-1]!="F" && states[lungimeStates-1]!="S")
        tipStates[n++]=0;

    int cst=0;
    if(states[lungimeStates]=="F")
        lungimeStates--,n--,cst=1;
    /*
    for(int i=0; i<n; i++)
    cout<<tipStates[i]<<"  ";
    cout<<endl;
    */

    //for(int i=0; i<lungimeStates; i++)
    //   cout<<states[i]<<endl;
    bool a[n][n];
    for(int i=0; i<n; i++)
        for(int j=0; j<n; j++)
            a[i][j]=0;
    for(int i=1; i<n; i++)
        for(int j=0; j<i; j++)
            if(tipStates[i] != tipStates[j])
                a[i][j]=1;
    bool ok;
    do
    {
        ok=0;
        for(int i=1; i<n; i++)
            for(int j=0; j<i; j++)
                if(a[i][j]==0)
                    for(int k=0; k<lungimeTransitions; k+=3)
                        if(transitions[k]==states[i])
                            for(int l=0; l<lungimeTransitions; l+=3)
                                if(transitions[l]==states[j])
                                    if(transitions[k+1]==transitions[l+1])
                                        for (int g=0; g<n; g++)
                                            if(states[g]==transitions[k+2])
                                                for (int h=0; h<n; h++)
                                                    if(states[h]==transitions[l+2])
                                                        if(a[g][h]==1 || a[h][g]==1)
                                                        {
                                                            a[i][j]=1;
                                                            ok=1;
                                                        }
    }
    while(ok==1);
    /*
    for(int i=1; i<n; i++)
    {
        for(int j=0; j<i; j++)
            cout<<a[i][j]<<" ";
        cout<<endl;
    }
    */
    cout<<"Sigma: "<<endl;
    for(int i=0; i<lungimeSigma; i++)
        cout<<sigma[i]<<endl;

    bool mark[n];
    for(int i=0; i<n; i++)
        mark[i]=0;
    cout<<"States: "<<endl;
    for (int j=0; j<n; j++)
    {
        if (mark[j]==0)
        {
            int verif=0;
            mark[j]=1;
            if (tipStates[j]==1)
                verif=1;
            else if (states[j]==start)
                verif=2;
            cout<<"{"<<states[j];
            for(int i=j+1; i<n; i++)
            {
                if(a[i][j]==0)
                {
                    cout<<","<<states[i];
                    if (tipStates[i]==1)
                        verif=1;
                    else if (states[i]==start)
                        verif=2;
                    mark[i]=1;
                }
            }
            cout<<"}";
            if (verif==1)
                cout<<",F";
            else if (verif==2)
                cout<<",S";
            cout<<endl;
        }
    }
    bool marcare[n];
    for(int i=0; i<n; i++)
        marcare[i]=0;
    cout<<"Transitions: "<<endl;
    for (int j=0; j<n; j++)
    {
        if(marcare[j]==0)
            for(int k=0; k<lungimeTransitions; k+=3)
                if(transitions[k]==states[j])
                {
                    ok=0;
                    marcare[j]=1;
                    cout<<"{"<<states[j];
                    for(int i=j+1; i<n; i++)
                    {
                        if(a[i][j]==0 && a[j][i]==0)
                        {
                            cout<<","<<states[i];
                            marcare[i]=1;
                            ok=1;
                        }
                    }
                    cout<<"}, "<<transitions[k+1];
                    for(int l=0; l<lungimeTransitions; l+=3)
                        if(transitions[l]==states[j] && transitions[k+1]==transitions[l+1])
                            for (int g=0; g<lungimeStates+cst; g++)
                                if(transitions[l+2]==states[g])
                                {
                                    cout<<", {"<<states[g];
                                    for(int i=0; i<n; i++)
                                    {
                                        if(a[i][g]==0 && a[g][i]==0 && states[i]!=states[g])
                                        {
                                            cout<<","<<states[i];
                                        }
                                    }
                                    cout<<"} "<<endl;
                                }
                }
    }
    return 0;
}
