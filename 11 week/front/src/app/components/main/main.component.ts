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
  public posts: Post[];
  public infoPost: Post;
  public likedPost: Post;

  constructor(private provider: ProviderService) { }

  ngOnInit() {
      this.provider.getPosts().then(res => {
         this.posts = res;
      });
  }
  
  getTasks(t: TaskList){
    return this.provider.getTasks(t).then( res => {
        this.tasks = res;
    });
  }

  getInfoPosts(c: Post){
    return this.provider.getInfoPosts(c).then(res => {
       this.infoPost = res;
    })
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
  deletePost(c: Post){
    this.provider.deletePost(c).then(res => {
      this.provider.getPosts().then(r => {
        this.posts = r;
      });
    });
  }

  likePost(c: Post){
     this.provider.likePost(c).then(res => {
       this.provider.getPosts().then(r => {
         this.posts = r;
       });
     });
  }
}
