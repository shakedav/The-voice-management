import { Injectable } from '@angular/core';
import {Http, Response} from "@angular/http";
import {Observable} from "rxjs";

@Injectable()
export class HttpService {

  constructor(private http: Http) { }

  public get(url: string) {
    return this.http.get(url)
      .map(this.extractData)
      .catch(this.handleError);
  }

  public post(url:string, data:any) {
    return this.http.post(url, data)
      .map(this.extractData)
      .catch(this.handleError);
  }


  private extractData(res: Response) {
    let response = res.json();
    return response || { };
  }

  private handleError (error: Response | any) {
    // In a real world app, you might use a remote logging infrastructure
    let errMsg: string;
    if (error instanceof Response) {
      const body = error.json() || '';
      const err = body.error || JSON.stringify(body);
      errMsg = `${error.status} - ${error.statusText || ''} ${err}`;
    } else {
      errMsg = error.message ? error.message : error.toString();
    }
    console.error(errMsg);
    return Observable.throw(errMsg);
  }

}
