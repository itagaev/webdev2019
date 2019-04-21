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
}
