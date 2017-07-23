import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CandidateActivitiesComponent } from './candidate-activities.component';

describe('CandidateActivitiesComponent', () => {
  let component: CandidateActivitiesComponent;
  let fixture: ComponentFixture<CandidateActivitiesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CandidateActivitiesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CandidateActivitiesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
