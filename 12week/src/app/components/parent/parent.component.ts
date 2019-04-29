import { Component, OnInit } from '@angular/core';
import { ProviderService } from 'src/app/shared/services/provider.service';
import { ICategory, IProduct } from 'src/app/shared/models/models';

@Component({
  selector: 'app-parent',
  templateUrl: './parent.component.html',
  styleUrls: ['./parent.component.css']
})
export class ParentComponent implements OnInit {
  public output:string = '';
  public stringArray: string[] = [];
  public categories: ICategory[] = [];
  public loading = false;
  public products: IProduct[] = [];

  constructor(private provider: ProviderService) { }
  

  ngOnInit() {
    this.provider.getCategories().then(res =>{
      
      this.categories = res;
      console.log(this.categories);
      setTimeout(() => {
        this.loading = true;
      }, 2000);
    });
  }

  getProducts(category: ICategory){
     
     this.provider.getProducts(category).then(res => {
         this.products = res;
         console.log(this.products);
     });
  }

  sendMessageService(){
    this.provider.sendMessage.emit("This message sent by Parent");
  }
}
