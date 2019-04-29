import { Component, OnInit } from '@angular/core';
import { ProviderService } from 'src/app/services/provider.service';

@Component({
  selector: 'aaa',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {
  public name: string = '';
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

  createTaskList(){
    if(this.name !== ''){
      this.provider.createTaskList(this.name).then(res => {
        this.name = '';
        this.taskLists.push(res);
      });
    }
  }
  deleteTaskList(tl: TaskList){
    this.provider.deleteTaskList(tl.id).then(res => {
        this.provider.getTaskLists().then(r => {
          this.taskLists = r;
        });
    });
  }
  updateTaskList(tl: TaskList){
     this.provider.updateTaskList(tl).then(res => {
         console.log(tl.name + 'updated!');
     });
  }
}
