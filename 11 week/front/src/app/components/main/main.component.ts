import { Component, OnInit } from '@angular/core';
import { ProviderService } from 'src/app/services/provider.service';

@Component({
  selector: 'aaa',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  public taskLists: TaskList[];
  public tasks: Task[];

  constructor(private provider: ProviderService) { }

  ngOnInit() {
    this.provider.getTaskLists().then( res => {
      
        this.taskLists = res;
        console.log(this.taskLists);
    });
  }
  
  getTasks(t: TaskList){
    return this.provider.getTasks(t).then( res => {
        this.tasks = res;
    });
  }
}
