import { Injectable } from '@angular/core';
import { MainService } from './main.service';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService{

  constructor(http: HttpClient) {
    super(http);
   }

   getTaskLists(): Promise<TaskList[]>{
     return this.get("http://localhost:8000/api/task_lists/", {});
   }

   getTasks(t: TaskList): Promise<Task[]>{
       return this.get("http://localhost:8000/api/task_lists/" + t.id + "/tasks", {});
   }

   createTaskList(name: string): Promise<TaskList>{
      return this.post("http://localhost:8000/api/task_lists/", {
        name: name
      });
   }

   updateTaskList(tl: TaskList): Promise<TaskList>{
     return this.put("http://localhost:8000/api/task_lists/" + tl.id + "/", {
        name: tl.name
     });
   }
   
   deleteTaskList(id: number): Promise<any>{
     return this.delet("http://localhost:8000/api/task_lists/" + id, {})
   }

   getPosts(): Promise<Post[]>{
     return this.get("http://localhost:8000/posts/", {})
   }

   getInfoPosts(c: Post): Promise<Post>{
       return this.get("http://localhost:8000/posts/" + c.id + "/", {})
   }

   deletePost(c: Post): Promise<any>{
    return this.delet("http://localhost:8000/posts/" + c.id + "/", {})
   }

   likePost(c: Post): Promise<Post>{
     return this.put("http://localhost:8000/posts/" + c.id + "/like", {
       'title': c.title,
       'body': c.body,
       'like_count': c.like_count + 1,
       'created_at': c.created_at,
       'created_by': c.created_by
     })
   }


}
